

const FIELD_ERROR = document.querySelector('.error');

// Подтверждение Да / Нет, срабатывание полученной функции
export function confirmсChanges(func, args){
  const modal = document.getElementById("confirmModal");
  const confirmBtn = document.getElementById("confirmBtn");
  const cancelBtn = document.getElementById("cancelBtn");

  modal.style.display = "block";

  confirmBtn.onclick = function() {
    func(...args);
    modal.style.display = "none";
  }

  cancelBtn.onclick = function() {
    modal.style.display = "none";
  }
}

// Обновление страницы
function reload() {
  window.location.reload(); 
}

// Вывод сообщения ошибки
function errorShow (msg="Какая-то ошибка") {
  FIELD_ERROR.innerHTML = msg;
}

// Отправка действий, данных на сервер
export function fetchPostPutDel(uri, data, method="POST") {
  let settings = {};
  settings.method = method;
  settings.headers = {'Content-type': 'application/json; charset=UTF-8'};
  settings.body = JSON.stringify(data);

  fetch(uri, settings)
    .then(response => {

      if (!response.ok) {
        return response.text().then(text => {throw new Error(`${text} ${response.status}`)})
      };
      reload(); 
      reload(); 
    })
    .catch(error => {
      console.log(error)
      console.error(error.message);
      errorShow(error);
  })
}

// Отправка действий, данных на сервер
export function fetchRenderJson(uri, render_field=undefined) {
  let settings = {};
  settings.headers = {'Content-type': 'text/html; charset=utf-8'};

  fetch(uri, settings)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      };

      const contentType = response.headers.get('Content-Type');
      const authorization = response.headers.get('Authorization'); 
 
      if (contentType && contentType.includes('application/json')) { 
        const res_json = response.json()
        return res_json;
      }
      throw new Error(`JSON error! not json`);
    })
    .then(res_json => {
        render_field.innerHTML = '';
        console.log(res_json);
        for (let item of res_json) {
          console.log(item);
          render_field.insertAdjacentHTML('beforeend', `<tr>
                                                            <td>${item[0]}</td>
                                                            <td>${item[1]}</td>
                                                            <td>${item[2]}</td>
                                                            <td>${item[3]}</td>
                                                            <td>${item[4]}</td>
                                                            <td>${item[5]}</td>
                                                        </tr>`); 
        }

    })
    .catch(error => {
      console.error('Код ошибки', error);
      errorShow();
  })
}


// Загрузить
export function downloadDB(uri) {
    fetch(uri)
    .then(response => {
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      return response.text();}
    )
    .catch(error => {
      console.error('Код ошибки', error);
      errorShow();}
    )
    
    console.log('--------------')
}


export const params = {
  menu1: 'menu1.html',
  menu2: 'menu2.html,',
  table: document.querySelector('[data-table]'),
  error: document.querySelector('.error'),
  fetchPostPutDel: fetchPostPutDel,
}
















// if ( method == "POST" ) {
//   fetch(uri, {
//     method:method,
//     body: JSON.stringify(data),
//     headers: {'Content-type': 'application/json; charset=UTF-8'},
//   })
//   .then(response => {
//     if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
//     return response.text(); 
//   })
//   .then(text => {
//     console.log(text); 
//   })
//   .catch(error => {
//     console.error('Код ошибки', error);
//     errorShow();
//   })
//   // .finally(() => reload);
// }





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




// const modal = document.getElementById("confirmModal");
// const confirmBtn = document.getElementById("confirmBtn");
// const cancelBtn = document.getElementById("cancelBtn");

// function openModal() {
//   modal.style.display = "block";
// }



// export function fetchPostPutDel(uri, 
//                                 data, 
//                                 method="POST", 
//                                 render_field=undefined) {
//   let settings = {};
//   settings.method = method;

//   if (method == 'GET') {
//     settings.headers = {'Content-type': 'text/html; charset=utf-8'}
//   } else {
//     settings.headers = {'Content-type': 'application/json; charset=UTF-8'};
//     settings.body = JSON.stringify(data)
//   }

//   fetch(uri, settings)
//     .then(response => {
//       if (!response.ok) {
//         throw new Error(`HTTP error! status: ${response.status}`)
//       };

//       const contentType = response.headers.get('Content-Type');
//       const authorization = response.headers.get('Authorization'); 

//       if (contentType && contentType.includes('application/json')) { 
//         let result = response.json();

//         console.log(result);
//         console.log('===========');
//       for (let key in result){
//           console.log('-----------');
//           console.log(key);
//         }
//       } 
//       else { reload(); }
//     })
//     .catch(error => {
//       console.error('Код ошибки', error);
//       errorShow();
//   })
// }

