

import { params, fetchPostPutDel, confirmсChanges } from "./app.js";


const URI = '/office'

// Добавление данных
function addData(e) {
  let item = e.target.closest('[data-item]');
  let office_name = item.querySelector('[data-office-name]');
  let data = {};

  if (office_name.value) {
    data.office_name = office_name.value;
    
    fetchPostPutDel(URI, data, 'POST');
  }
}

// Изменение данных
function upateData(e) {
  let item = e.target.closest('[data-item]');
  let office_number = item.querySelector('[data-office-number]').innerHTML;
  let office_name = item.querySelector('[data-office-name]');
  let data = {};

  if (office_name.dataset.officeName != office_name.value) {
    data.office_number = office_number;
    data.office_name = office_name.value;

    confirmсChanges(fetchPostPutDel, [URI, data, 'PUT']);
  }
}

// Удаление данных
function deleteData(e) {
  let item = e.target.closest('[data-item]');
  let office_number = item.querySelector('[data-office-number]').innerHTML;
  let data = {};

  data.office_number = office_number;

  confirmсChanges(fetchPostPutDel, [URI, data, 'DELETE']);
}

// Определение какое действие выбрано, подтверждение действия
function chooseData(e) {
  e.preventDefault();

  if (!e.target.matches('[data-update], [data-delete], [data-add]')){
    return 
  } 
  
  if (e.target.matches('[data-add]')){
    addData(e); 
  } else if (e.target.matches('[data-update]')){
    upateData(e);
  } else if (e.target.matches('[data-delete]')){
    deleteData(e);
  }
}

// Обработка действий
params.table?.addEventListener('click', chooseData);






















