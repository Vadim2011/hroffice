

import { downloadDB } from "./app.js";
import { params, fetchPostPutDel, confirmсChanges, fetchRenderJson} from "./app.js";


const RENDER_FIELD = document.querySelector('[data-table]');
const URI = '/get-child'
const btnDownload = document.querySelector('[data-download]');


btnDownload?.addEventListener('click', () => {
  const indexOffice = document.querySelector('[data-select-office]');
  let url = indexOffice ? URI + '/' + indexOffice.value : URI;
  
  fetchRenderJson(url, RENDER_FIELD);
})



