class so{
    static void pln(Object o){System.out.println(o.toString());}
}

abstract class DemoAbstractClass {
    abstract void display();
    abstract boolean checkPalindrome(String s);
}

class StringWork extends DemoAbstractClass{
    String str;
    StringWork(String s){
        str = s;
    }
    void display(){
        so.pln(str);
    }
    boolean checkPalindrome(String s){
        return true;
    }
}

class Main {
    public static void main(String[] args) {
        StringWork sw = new StringWork("hello");
        so.pln(sw.checkPalindrome("hello"));
    }
}
