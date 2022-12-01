class Base
{
    public void abc()
    {
        System.out.println("hello");
    }
}

class Derived extends Base
{
    public void abc()
    {
        System.out.println("hello from derived");
    }
}

public class Override {
    public static void main(String[] args) {
        Derived der = new Derived();
        der.abc();
    }
}
