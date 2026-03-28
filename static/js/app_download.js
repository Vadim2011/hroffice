

import { downloadDB } from "./app.js";



const URI = '/download'
const btnDownload = document.querySelector('[data-download]');
btnDownload?.addEventListener('click', () => downloadDB(URI));




