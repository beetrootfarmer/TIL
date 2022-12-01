

public class GameMachine {
    private int coin;
    public GameMachine(int coin)
    {
        this.coin = coin;
        coinNow();
    }
    public void inputCoin(int input)
    {
        if (input > 5) {
            return;
        } 
        this.coin += input;
        coinNow();
    }
    public void playGame()
    {
        System.out.println("게임진행..");
        this.coin -= 1;
        coinNow();
    }
    public void coinNow()
    {
        System.out.println("현재 코인.."+ coin);
    }
    public static void main(String[] args) {
        GameMachine gm = new GameMachine(5);
        gm.inputCoin(5);
        gm.playGame();
    }
}

