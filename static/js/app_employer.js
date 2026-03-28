import { params, fetchPostPutDel, confirmсChanges } from "./app.js";


const URI = '/employer'



// Добавление данных
function addData(e) {
  let item = e.target.closest('[data-item]');
  let employer_surname = item.querySelector('[data-employer-surname]');
  let employer_firstname = item.querySelector('[data-employer-firstname]');
  let employer_patronymic = item.querySelector('[data-employer-patronymic]');
  let employer_gender = item.querySelector('[data-employer-gender]');
  let employer_length_work = item.querySelector('[data-employer-length-work]');
  let office_number = item.querySelector('[data-office-number]');

  let data = {};

  if ( employer_surname.value && 
      employer_firstname.value &&
      // employer_patronymic.value &&
      employer_gender.value &&
      employer_length_work.value &&
      office_number.value ) {
    data.employer_surname = employer_surname.value;
    data.employer_firstname = employer_firstname.value;
    data.employer_patronymic = employer_patronymic.value;
    data.employer_gender = employer_gender.value;
    data.employer_length_work = employer_length_work.value;
    data.office_number = office_number.value;
    
    fetchPostPutDel(URI, data, 'POST');
  }
}

// Изменение данных
function upateData(e) {
  let item = e.target.closest('[data-item]');
  let employer_number = item.querySelector('[data-employer-number]').innerHTML;
  let employer_surname = item.querySelector('[data-employer-surname]');
  let employer_firstname = item.querySelector('[data-employer-firstname]');
  let employer_patronymic = item.querySelector('[data-employer-patronymic]');
  let employer_gender = item.querySelector('[data-employer-gender]');
  let employer_length_work = item.querySelector('[data-employer-length-work]');
  let office_number = item.querySelector('[data-office-number]');

  let data = {};

  if (employer_surname.dataset.employerSurname != employer_surname.value) data.employer_surname = employer_surname.value;
  if (employer_firstname.dataset.employerFirstname != employer_firstname.value) data.employer_firstname = employer_firstname.value;
  if (employer_patronymic.dataset.employerPatronymic != employer_patronymic.value) data.employer_patronymic = employer_patronymic.value;
  if (employer_gender.dataset.employerGender != employer_gender.value) data.employer_gender = employer_gender.value;
  if (employer_length_work.dataset.employerLengthWork != employer_length_work.value) data.employer_length_work = employer_length_work.value;
  if (office_number.dataset.officeNumber != office_number.value) data.office_number = office_number.value;

  if ( Object.keys(data).length ) {    
    data.employer_number = employer_number;
    
    confirmсChanges(fetchPostPutDel, [URI, data, 'PUT']);
  }
}

// Удаление данных
function deleteData(e) {
  let item = e.target.closest('[data-item]');
  let employer_number = item.querySelector('[data-employer-number]').innerHTML;
  let data = {};

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