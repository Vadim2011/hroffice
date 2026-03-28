
const FIELD_ERROR = document.querySelector('.error');

function reload() {
  window.location.reload(); 
}

function errorShow (msg="Какая-то ошибка") {
  FIELD_ERROR.innerHTML = msg;
}

function fetchPut (uri, content) {
  fetch(uri,{
    method: 'PUT',
    body: JSON.stringify(content),
    headers: {'Content-type': 'application/json; charset=UTF-8',},
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json(); 
  })
  .then(data => {
    console.log(data); 
  })
  .catch(error => {
    console.error('Код ошибки', error);
    errorShow();
  });
}

function fetchDelete(uri, itemId) {
  fetch(uri + `/${itemId}`, {
    method: 'DELETE'
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return  
  })
  .catch(error => {
    console.error('Код ошибки', error);
    errorShow();
  });
}

function fetchPost(uri, content) {
  fetch(uri,{
    method: 'POST',
    body: JSON.stringify(content),
    headers: {'Content-type': 'application/json; charset=UTF-8',},
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json(); 
  })
  .then(data => {
    console.log(data); 
  })
  .catch(error => {
    console.error('Код ошибки', error);
    errorShow();
  })
  .finally(() => reload);
}


function upateData(e) {
  let item = e.target.closest('[data-item]');
  let idItem = item.querySelector('[data-id]').innerHTML;
  let itemOffice = item.querySelector('[data-name-office]');

  let itemField = {};

  if (itemOffice.dataset.nameOffice != itemOffice.value) {
    itemField.id = idItem;
    itemField.nameOffice = itemOffice.value;

    fetchPut('uri',itemField);
  }

}

function deleteData(e) {
  let item = e.target.closest('[data-item]');
  let idItem = item.querySelector('[data-id]').innerHTML;

  fetchDelete('uri', idItem);
  
}

function addData(e) {
  let item = e.target.closest('[data-item]');
  let itemOffice = item.querySelector('[data-name-office]');
  let itemField = {};

  if (itemOffice.value) {
    itemField.nameOffice = itemOffice.value;
    fetchPost('uri', itemField);
  }
}

function chooseData(e) {
  if (!e.target.matches('[data-update], [data-delete], [data-add]')){
    return 
  } 

  if (e.target.matches('[data-update]')){
    upateData(e);
  } else if (e.target.matches('[data-delete]')){
    deleteData(e);
  } else if (e.target.matches('[data-add]')){
    addData(e); 
  }
}


let table = document.querySelector('[data-table]');
table?.addEventListener('click', chooseData);







