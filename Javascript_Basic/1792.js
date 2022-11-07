const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]
const game = participantNums.length
for(g of participantNums){
    for (i in g){
        let idx = Number(i)
        let num = g[idx]
        g[idx]= 0
        if (g.indexOf(num) != -1){
            g[g.indexOf(num)] = 0
        } else {
            console.log(num)
            break
        }
    }
}

// 3
// 100
// 62
