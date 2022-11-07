/* 
  아래에 코드를 작성해주세요.
*/
const input = document.querySelector('.search-box__input')
const button = document.querySelector('.search-box__button')
const resultBox = document.querySelector('.search-result')
let pre = ''

// infinite scroll
const sentinel = document.createElement('div')
sentinel.id = 'sentinel'
createObserver(sentinel)

async function fetchAlbums(page = 1){
  
  // Loader
  const loadingList = document.querySelector('.search-result--loadingList')
  loadingList.style.display = 'block'
  
  const keyWord = input.value
  if (!keyWord.trim()) return
  // exception! 페이지 새로고침 하지 않아도 재 검색이 가능하도록
  if (pre !== keyWord){
    resultBox.innerHTML = ''
    pre = keyWord
  }
  
  const API_KEY = '90ba585301fe6995e3cfd255a0039d7a'
  const BASE_URL = 'https://ws.audioscrobbler.com/2.0/'
  const searchUrl = `?method=album.search&format=json`
  
  const requestUrl = BASE_URL + searchUrl
  
  axios({
    url: requestUrl,
    method : 'POST',
    params : {
      api_key : API_KEY,
      album : keyWord,
      page :1 ,
      limit : 100,
    },
    
  }).then((response) => {
    // (advanced) 로더
    loadingList.style.display = 'none'
    
    console.log('왔다')
    console.log(response.data.results.albummatches.album)
    let albums = response.data.results.albummatches.album
    
    // exception 검색 결과가 없을 때
    if (!albums.length){
      resultBox.innerHTML = `
      "${keyWord}"<span style="color: grey;">에 대한 검색 결과가 없습니다.</span>
      `
      return
      
    }
    for ( al of albums ){
      const cardImg = document.createElement('img')
      cardImg.src = al.image[1]['#text']
      
      const card = document.createElement('div')
      card.classList.add('search-result__card')
      
      const cardText = document.createElement('div')
      card.classList.add('search-result__text')
      const artist = document.createElement('p')
      artist.innerText = al.artist // 아티스트 이름
      const albumTitle = document.createElement('h2')
      albumTitle.innerText = al.name // 앨범 이름 
      cardText.append(artist, albumTitle)
      
      card.append(cardImg, cardText)
      resultBox.append(card)
      resultBox.append(sentinel) // infinity scroll
      card.addEventListener('click', () => {
        window.location.href = al.url
      })
    }
  })
  .catch((error) => {
    alert('잠시 후 다시 시도해주세요')
  })
}

// infinite scroll
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

input.addEventListener('keypress', (e) => {
  if (e.keyCode === 13) fetchAlbums()
})
button.addEventListener('click', fetchAlbums)