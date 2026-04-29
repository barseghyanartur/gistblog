(function() {
        var navSearchLink = document.getElementById("nav-search-link");
        var searchDropdown = document.getElementById("search-dropdown");
        var searchInput = document.getElementById("search-dropdown-input");
        var resultsContainer = document.getElementById("search-dropdown-results");

        var lunrIndex = null;
        var documentsData = [];
        var indexLoaded = false;
        var dropdownOpen = false;

        var SITEURL = "{{ SITEURL }}";
        var baseUrl = SITEURL ? (SITEURL.endsWith("/") ? SITEURL : SITEURL + "/") : "/";
        var searchIndexUrl = baseUrl + "static/search_index.json";

        function initSearch() {
                if (indexLoaded) return;
                indexLoaded = true;

                fetch(searchIndexUrl)
                        .then(function(response) {
                                if (!response.ok) throw new Error("Failed to load search index");
                                return response.json();
                        })
                        .then(function(data) {
                                documentsData = data;

                                lunrIndex = lunr(function() {
                                        this.ref("url");
                                        this.field("title", { boost: 15 });
                                        this.field("content", { boost: 10 });
                                        this.field("summary", { boost: 8 });
                                        this.field("tags", { boost: 6 });
                                        this.field("category", { boost: 3 });

                                        documentsData.forEach(function(doc) { this.add(doc); }, this);
                                });

                                resultsContainer.innerHTML = '<div class="search-dropdown-hint">Type to search...</div>';
                        })
                        .catch(function(err) {
                                console.error(err);
                                resultsContainer.innerHTML = '<div class="search-dropdown-hint">Search unavailable</div>';
                        });
        }

        function performSearch(query) {
                var fullLink = document.getElementById("search-full-link");

                if (!query || query.trim() === "") {
                        resultsContainer.innerHTML = '<div class="search-dropdown-hint">Type to search...</div>';
                        fullLink.href = baseUrl + "search.html";
                        return;
                }

                fullLink.href = baseUrl + "search.html?q=" + encodeURIComponent(query);

                if (!lunrIndex) {
                        resultsContainer.innerHTML = '<div class="search-dropdown-hint">Loading...</div>';
                        return;
                }

                var results = lunrIndex.search(query);
                var maxResults = 3;

                if (results.length === 0) {
                        resultsContainer.innerHTML = '<div class="search-dropdown-hint">No matching posts found.</div>';
                        return;
                }

                var html = "";
                var slice = results.slice(0, maxResults);
                for (var i = 0; i < slice.length; i++) {
                        var result = slice[i];
                        var doc = null;
                        for (var j = 0; j < documentsData.length; j++) {
                                if (documentsData[j].url === result.ref) {
                                        doc = documentsData[j];
                                        break;
                                }
                        }
                        if (!doc) continue;

                        var fullUrl = baseUrl + (doc.url.startsWith("/") ? doc.url.slice(1) : doc.url);

                        html += '<a href="' + fullUrl + '" class="search-dropdown-result">' +
                                '<span class="search-dropdown-result-title">' + doc.title + '</span>' +
                                '<span class="search-dropdown-result-meta">' + doc.date + ' &bull; ' + doc.category + '</span>' +
                        '</a>';
                }

                if (results.length > maxResults) {
                        html += '<div class="search-dropdown-more">' +
                                '+' + (results.length - maxResults) + ' more results' +
                        '</div>';
                }

                resultsContainer.innerHTML = html;
        }

        function openDropdown() {
                dropdownOpen = true;
                searchDropdown.classList.add("open");
                navSearchLink.classList.add("active");
                initSearch();
                setTimeout(function() { searchInput.focus(); }, 50);
        }

        function closeDropdown() {
                dropdownOpen = false;
                searchDropdown.classList.remove("open");
                navSearchLink.classList.remove("active");
        }

        navSearchLink.addEventListener("click", function(e) {
                e.preventDefault();
                if (dropdownOpen) {
                        closeDropdown();
                } else {
                        openDropdown();
                }
        });

        document.addEventListener("click", function(e) {
                if (!searchDropdown.contains(e.target) && e.target !== navSearchLink) {
                        closeDropdown();
                }
        });

        document.addEventListener("keydown", function(e) {
                if (e.key === "Escape") {
                        closeDropdown();
                }
        });

        var timeout;
        searchInput.addEventListener("input", function() {
                clearTimeout(timeout);
                timeout = setTimeout(function() {
                        performSearch(searchInput.value);
                }, 150);
        });
})();
