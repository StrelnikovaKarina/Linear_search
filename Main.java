class Thread_ implements Runnable {
    Thread_() {
        Thread thread1 = Thread.currentThread();
        Thread thread2 = new Thread(this);
        // запускается поток thread2
        thread2.start();
        try {
            for (int i = 5; i > 0; i--) {
                System.out.println("thread2 run " + i);
                Thread.sleep(1000);
            }
        } catch (InterruptedException e) {
        }
    }
    // выполнение thread1
    public void run() {
        try {
            for (int i = 10; i > 0; i--) {
                System.out.println("thread1 run " + i);
                Thread.sleep(500);
            }
        } catch (InterruptedException e) {
        }
    }
    public static void main(String args[]) {
        new Thread_();
    }
}