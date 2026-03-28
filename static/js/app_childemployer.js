import { params, fetchPostPutDel, confirmсChanges } from "./app.js";


const URI = '/childemployer'



// Добавление данных
function addData(e) {
  let item = e.target.closest('[data-item]');
  let child_birth_cert_number = item.querySelector('[data-child-birth-cert-number]');
  let employer_number = item.querySelector('[data-employer-number]');
  let child_name = item.querySelector('[data-child-name]');
  let child_birth_year = item.querySelector('[data-child-birth-year]');
  let child_gender = item.querySelector('[data-child-gender]');

  let data = {};

  if ( child_birth_cert_number.value && employer_number.value &&
        child_name.value && child_birth_year.value && child_gender.value ) {
    data.child_birth_cert_number = child_birth_cert_number.value;
    data.employer_number = employer_number.value;
    data.child_name = child_name.value;
    data.child_birth_year = child_birth_year.value;
    data.child_gender = child_gender.value;
    
    fetchPostPutDel(URI, data, 'POST');
  }
}

// Изменение данных
function upateData(e) {
  let item = e.target.closest('[data-item]');
  let child_birth_cert_number = item.querySelector('[data-child-birth-cert-number]');
  let employer_number = item.querySelector('[data-employer-number]');
  let child_name = item.querySelector('[data-child-name]');
  let child_birth_year = item.querySelector('[data-child-birth-year]');
  let child_gender = item.querySelector('[data-child-gender]');

  let data = {};

  if (child_birth_cert_number.dataset.childBirthCertNumber != child_birth_cert_number.value) data.child_birth_cert_number = child_birth_cert_number.value;
  if (employer_number.dataset.employerNumber != employer_number.value) data.employer_number = employer_number.value;
  if (child_name.dataset.childName != child_name.value) data.child_name = child_name.value;
  if (child_birth_year.dataset.childBirthYear != child_birth_year.value) data.child_birth_year = child_birth_year.value;
  if (child_gender.dataset.childGender != child_gender.value) data.child_gender = child_gender.value;
  if ( Object.keys(data).length ) {    
    
    data.child_birth_cert_number = child_birth_cert_number.value;
    data.employer_number = employer_number.value;

    confirmсChanges(fetchPostPutDel, [URI, data, 'PUT']);
  }
}

// Удаление данных
function deleteData(e) {
  let item = e.target.closest('[data-item]');
  let child_birth_cert_number = item.querySelector('[data-child-birth-cert-number]').value;
  let employer_number = item.querySelector('[data-employer-number]').value;
  let data = {};

  data.child_birth_cert_number = child_birth_cert_number;
  data.employer_number = employer_number;

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