document.querySelectorAll('form').forEach((el) => {
  el.addEventListener('submit', _ => {
    let divCarregamento = document.getElementById('carregamento');
    divCarregamento.classList.remove('d-none');
  })
});

function setValueInURL(name, value, url) {
  if (url == undefined) {
    url = new URL(window.location.href);
  }
  url.searchParams.set(name, value);
  return url;
}

function toPage(page_number) {
  window.location = setValueInURL('page', page_number)
}
