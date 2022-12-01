class Marin {
    public int hp = 100;
    // 메서드 생성
    public void run()
    {
        hp -=10;
        System.out.println("RUN " + hp);
    }
    // 리턴 타입이 없는 것은 생성자
    // 인자로 받은 hp로 해당 인스턴스의 속성을 초기화 할 수 있도록함
    public Marin(int hp)
    {
        this.hp = hp;
    }
}

class Zergling {
    public int hp = 80;
    public int mana = 200;

    public void attack()
    {
        hp += 1;
        mana -= 10;
    }

    public void move()
    {
        hp -= 10;
        mana += 5;
    }
    public void status()
    {
        System.out.println("현재 hp = " + hp);
        System.out.println("현재 mana = " + mana);
    }
}

public class Main{
    public static void main(String[] args) {
        // Marin 객체 생성(인스턴스화) ... 생성자 호출
        Marin m1 = new Marin(100);
        
        System.out.println(m1.hp);
        m1.run();
        m1.run();

        System.out.println("_________도전과제___________");
        Zergling z1 = new Zergling();
        Zergling z2 = new Zergling();
        z1.status();
        System.out.println("z1 attacked");
        z1.attack();
        z1.status();

        z2.status();
        System.out.println("z2 moved");
        z2.move();
        z2.status();
    }
}