
const SUBMIT_LOGIN = document.querySelector('.submit');
const FIELD_ERROR = document.querySelector('.error');

function reload() {
  window.location.reload(); 
}

function errorShow (msg="Какая-то ошибка") {
  FIELD_ERROR.innerHTML = msg;
}


function check_login_pass(e) {
  e.preventDefault();

  const role = document.forms['login'].elements['role_'].value;
  const passw = document.forms['login'].elements['passw'].value;

  if ( role == 'hr') {
    if (passw == '123') {
      errorShow('');
      window.location.href = '/menu2.html';
    } else {
      errorShow('УКАЗАН НЕВЕРНЫЙ ПАРОЛЬ');
    }
  } 
  
  else if (role == 'manager') {
    if (passw == '321') {
      errorShow('');
      window.location.href = '/menu1.html';
    } else {
      errorShow('УКАЗАН НЕВЕРНЫЙ ПАРОЛЬ');
    }
  } else {
    errorShow('УКАЗАН НЕВЕРНЫЙ ПАРОЛЬ ИЛИ РОЛЬ');
  }
}


// SUBMIT_LOGIN.addEventListener('click', check_login_pass);





