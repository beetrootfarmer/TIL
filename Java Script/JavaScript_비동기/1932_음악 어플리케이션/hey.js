let page = 1 
let limit = 100
let prevKeyword = ''
const searchInput = document.querySelector('.search-box__input')
const searchBtn = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')  

searchInput.addEventListener('keypress', (e) => {
  if (e.keyCode === 13) fetchAlbums()
})
searchBtn.addEventListener('click', fetchAlbums)

const sentinel = document.createElement('div')
sentinel.id = 'sentinel'
createObserver(sentinel)

async function fetchAlbums(page=1, limit=100) {
  // (advanced) 로더
  const loadingList = document.querySelector('.search-result--loadingList')
  loadingList.style.display = 'block'

  const keyword = searchInput.value
  if (!keyword.trim()) return
  
  // (exception) 새로운 검색어일 경우 기존 결과 초기화
  if (prevKeyword !== keyword) {
    searchResult.innerHTML = ''
    prevKeyword = keyword
  }
  
  const API_KEY = '15765d1dbbb01e2baaef37788b01cf5f'
  const BASE_URL = 'https://ws.audioscrobbler.com/2.0/'
  const searchUrl = `?method=album.search&format=json`
  const params = {
    api_key: API_KEY,
    album: keyword,
    page: 1,
    limit: 100,
  }
  
  const requestUrl = BASE_URL + searchUrl
  const res = await axios.get(requestUrl, { params })
  const albums = res.data.results.albummatches.album
  
  // (advanced) 로더
  loadingList.style.display = 'none'
  
  // (exception) 검색 결과가 없을 때
  if (!albums.length) {
    searchResult.innerHTML = `
      "${keyword}"<span style="color: grey;">에 대한 검색 결과가 없습니다.</span>
    `
    return
  }
  appendAlbumCards(albums)
}

function appendAlbumCards(albums) {
  const cardList = document.createDocumentFragment() // Optimized Version
  albums.forEach(album => {  
    
    // left side's image tag
    const cardImgSrc = album.image[1]['#text']
    const cardImg = document.createElement('img')
    cardImg.src = cardImgSrc
    cardImg.alt = '앨범 이미지'

    // (exception) 앨범 이미지 없을 경우
    if (!cardImgSrc) cardImg.src = './assets/default.png'
    
    // right side content
    const cardArtistName = document.createElement('h2')
    const cardAlbumName = document.createElement('p')
    cardArtistName.innerText = album.artist
    cardAlbumName.innerText = album.name
    
    // right side box
    const cardText = document.createElement('div')
    cardText.classList.add('search-result__text')
    cardText.append(cardArtistName, cardAlbumName)
    
    // card (left + right)
    const card = document.createElement('div')
    card.classList.add('search-result__card')
    card.append(cardImg, cardText)
    card.addEventListener('click', () => {
      window.location.href = album.url
    })

    cardList.appendChild(card)
  })
  
  searchResult.append(cardList)
  searchResult.append(sentinel) // (advanced) Infinite Scrolling
}


/* 
  ===== 
  (advanced) Infinite Scrolling
  =====
*/
function createObserver(target) {
  const getMoreAlbums = (entries) => {
    entries.forEach(entrie => {
      if (entrie.isIntersecting) {
        page += 1
        fetchAlbums(page)
      }
    })
  }
  
  const observer = new IntersectionObserver(getMoreAlbums);
  observer.observe(target); 
}
