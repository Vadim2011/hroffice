
const FIELD_ERROR = document.querySelector('.error');

function reload() {
  window.location.reload(); 
}

function errorShow (msg="Какая-то ошибка") {
  FIELD_ERROR.innerHTML = msg;
}



let urioffice = 'http://localhost/api/v1/offices/';
let uriemployer = 'http://localhost/api/v1/employers/';
let urichildemp = 'http://localhost/api/v1/childemp/';

let uriselect =  'http://localhost/api/v1/offices/{id}';

let urialldb =  'http://localhost/api/v1/offices/doc/';
let urioffchild = 'http://localhost/api/v1/offices/doc/{id}'


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
    console.error('An error occurred:', error);
  });
}




















// // GET  POST  PUT  DELETE  
// // PATCH  CONNECT  OPTIONS  HEAD
// // fetch современный метод для выполнения
// // AJAX (Asynchronous JavaScript and XML)
// // 

// // let promise = fetch(url, [options]);

// let url = 'http://127.0.0.1:5500/menu2.html';
// let promise = fetch(url);

// promise
// .then(response => {
//   console.log(response.ok);
//   console.log(response.status);
//   // window.location.href ='menu1.html';
// })
// .catch(error => console.log(error.message));


// // button.addEventListener('click', function (){
// //   fetch(url)
// //     .then(response => response.json())
// //     .then(json => {
// //       output.innerHTML = 'asdfasdf' + json.title;
// //       output.innerHTML = 'asdfasdf' + json.userID;
// //     })
// // })

// // r.text()
// // r.json()
// // r.formData()
// // r.arrayBuffer()






// let request = fertch(url, {
//   headers: {
//     Accept: 'text/plain'
//   }
// });

// b.addEventListener('click', function () {
//   let url = 'localhost/office';
//   let task = {
//     userId:123,
//     title: 'Testtask',
//     complete: false,
//   };

//   fetch(url, {
//     method: 'POST',
//     body: JSON.stringify(task),
//     headers: {
//       'Content-type': 'application/json; charset=UTF-8',
//     },
//   })
//     .then((response) =>response.json())
//     .then((json) => console.log(json));
// })

// let url_1 = 'localhost/todo';
// let load_button = document.querySelector('#loadbutton');
// let loader = document.querySelector('#loader');
// let todo_list = document.querySelector('#todo');

// load_button.addEventListener('click', function() {
//   showLoader();
//   fetch(url_1)
//     .then(response => response.json())
//     .then(json => renderList(json))
//     .finally(hideLoader);
// });

// function showLoader() {
//   loader.style.display = 'inline';
// }

// function hideLoader() {
//   loader.style.display = 'none';
// }

// function renderList(list) {
//   list.forEach(element => {
//     let div = document.createElement('div');
//     div.innerHTML = `${element.id} ${element.complete}` ;

//     if (element.complete) {
//       div.classList.add('completed');
//     }
//     else {
//       div.classList.add('incomplete');
//     }
    
//     todo_list.append(div);
//   });
// }



// document.getElementById('myForm').addEventListener('submit', function(event) {
//   event.preventDefault(); // Остановить стандартную отправку формы

//   const formData = new FormData(this);
  
//   // Отправка данных
//   fetch('/api/submit', {
//       method: 'POST',
//       body: formData
//   })
//   .then(response => {
//       if (response.ok) {
//           // Обновление страницы после успешного ответа
//           window.location.reload(); 
//       } else {
//           console.error('Ошибка отправки');
//       }
//   })
//   .catch(error => console.error('Ошибка:', error));
// });




