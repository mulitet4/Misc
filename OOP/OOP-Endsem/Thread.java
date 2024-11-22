class so{
    static void pln(Object o){System.out.println(o.toString());}
}

class Resource {
    int[] evenNumbers = new int[6];
    int[] oddNumbers = new int[6];
}

class P1 implements Runnable {
    Resource r;
    Thread t;
    
    P1(Resource r){
        this.r = r;
        t = new Thread(this);
        t.start();
    }
    
    public void run(){
        int j = 0;
        for (int i = 11; i <= 21; i++) {
            if (i % 2 == 0) {
                synchronized(r){
                    r.evenNumbers[j] = i;
                    try{Thread.sleep(1000);}catch(Exception e){}
                    j++;
                }
            }
        }
    }
}

class P2 implements Runnable{
    Resource r;
    Thread t;
    
    P2(Resource r){
        this.r = r;
        t = new Thread(this);
        t.start();
    }
    
    public void run(){
        int j = 0;
        for (int i = 11; i <= 21; i++) {
            if (i % 2 != 0) {
                synchronized(r){
                    r.oddNumbers[j] = i;
                    j++;
                }
            }
        }
    }
}

class P3 implements Runnable{
    Thread t;
    Resource r;
    Thread t1, t2;
    
    P3(Resource r, Thread t1, Thread t2){
        this.r = r;
        this.t1 = t1; this.t2 = t2;
        t = new Thread(this);
        t.start();
    }
    
    public void run(){
        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        for(int i: r.evenNumbers){so.pln(i);}
        for(int i: r.oddNumbers){so.pln(i);}
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        // Shared resources to hold even and odd numbers
        int[] evenNumbers = new int[6];
        int[] oddNumbers = new int[6];
        Resource r = new Resource();

        P1 p1 = new P1(r);
        P2 p2 = new P2(r);
        P3 p3 = new P3(r, p1.t, p2.t);

        // Ensure the main thread waits for P3 to complete
        p3.t.join();
    }
}


// 12
// 14
// 16
// 18
// 20
// 0
// 11
// 13
// 15
// 17
// 19
// 21