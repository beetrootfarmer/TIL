const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const playGame = (p1_choice, p2_choice) => {
	// 작성해 주세요
    const game = p1.length
    const rockScissorsPaper = {'rock':1, 'scissors':0, 'paper':2}
    for (i = 0; i < game; i++){
        if (p1[i] == 'scissors' && p2[i] == 'paper'){
            console.log('1')
        } else if(p2[i] == 'scissors' && p1[i] == 'paper'){
            console.log('2')
        } else if (p1[i] == p2[i]){
            console.log('무승부')
        } else {
            if (rockScissorsPaper[p1[i]] > rockScissorsPaper[p2[i]]){
                console.log('1')
            } else {
                console.log('2')
            }
        }
    }
}
playGame(p1, p2)
// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2