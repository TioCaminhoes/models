const searchInput = document.querySelector("#book-search");
const bookCards = [...document.querySelectorAll(".book-card[data-availability]")];
const filterButtons = [...document.querySelectorAll(".filter-tab")];
const resultsLabel = document.querySelector("#results-label");
const searchEmpty = document.querySelector("#search-empty");
const bookList = document.querySelector("#book-list");

let activeFilter = "all";

function updateBooks() {
    const query = searchInput.value.trim().toLocaleLowerCase("pt-BR");
    let visibleCount = 0;

    for (const card of bookCards) {
        const matchesQuery = card.dataset.search.includes(query);
        const matchesFilter = activeFilter === "all" || card.dataset.availability === activeFilter;
        const isVisible = matchesQuery && matchesFilter;
        card.hidden = !isVisible;
        if (isVisible) visibleCount += 1;
    }

    resultsLabel.textContent = `Exibindo ${visibleCount} ${visibleCount === 1 ? "livro" : "livros"}`;
    searchEmpty.hidden = visibleCount !== 0 || bookCards.length === 0;
    bookList.hidden = bookCards.length === 0 || visibleCount === 0;
}

searchInput?.addEventListener("input", updateBooks);

for (const button of filterButtons) {
    button.addEventListener("click", () => {
        activeFilter = button.dataset.filter;
        for (const filterButton of filterButtons) {
            const isSelected = filterButton === button;
            filterButton.classList.toggle("is-selected", isSelected);
            filterButton.setAttribute("aria-pressed", String(isSelected));
        }
        updateBooks();
    });
}

document.addEventListener("keydown", (event) => {
    if (event.key === "/" && document.activeElement !== searchInput) {
        event.preventDefault();
        searchInput?.focus();
    }
});
