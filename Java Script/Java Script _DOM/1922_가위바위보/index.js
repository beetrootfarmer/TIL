// 코드를 작성해 주세요
const scissors = document.querySelector('#scissors-button')
const rock = document.querySelector('#rock-button')
const paper = document.querySelector('#paper-button')
const modalBox = document.querySelector('.modal')
const modalCont = document.querySelector('.modal-content')
const playerImg = document.querySelector('#player1-img')
const comImg = document.querySelector('#player2-img')
const rockScissorsPaper = {'rock':1, 'scissors':0, 'paper':2}



const playGame = (user) => {
    // 컴퓨터의 랜덤 가위바위보 선택 후 출력
    // 가위바위보 이미지가 3초동안 바뀌다가
    
    let computer = Math.floor(Math.random() * 3)
    switch (computer){
        case 0 : comImg.src = "./img/scissors.png"; break;
        case 1 : comImg.src = "./img/rock.png"; break;
        case 2 : comImg.src = "./img/paper.png"; break;
    }
    // console.log(user, rockScissorsPaper[Number(computer)])
    let users = rockScissorsPaper[user]
    computer = Number(computer)
    let result = ''
    console.log(users, computer)
    // 승부 결정
    if (users == 0 && computer == 2){
        result = '당신의 승리입니다'
    } else if(users == 2 && computer == 0){
        result = '컴퓨터의 승리입니다'
    } else if (users == computer){
        result = '무승부입니다'
    } else {
        if (users > computer){
            result = '당신의 승리입니다'
        } else {
            result = '컴퓨터의 승리입니다'
        }
    }
    console.log("결과:" ,result)
    // modal로 결과 띄우기
    modalCont.innerText = result
    modalBox.style.display = "flex"
    modalBox.addEventListener('click',(e)=>{
        modalBox.style.display = "none"
    })
}
function comcom(b){
    comImg.src = "./img/scissors.png"
    comImg.src = "./img/rock.png"
    comImg.src = "./img/paper.png"
}

// 1. user가 선택한 사진 #player1-img에 띄우기 
scissors.addEventListener('click', (e) => {
    playerImg.setAttribute('src', "./img/scissors.png")
    setInterval(comcom(scissors), 3000)
    setTimeout(playGame('scissors'),30000)
})
rock.addEventListener('click', (e) => {
    playerImg.setAttribute('src', "./img/rock.png")
    comcom(rock)
    setTimeout(playGame('rock'),3000)
})
paper.addEventListener('click', (e) => {
    playerImg.setAttribute('src', "./img/paper.png")
    comcom(paper)
    setTimeout(playGame('paper'),3000)
})
// rock.addEventListener('click', playGame('rock'))
// paper.addEventListener('click', playGame('paper'))