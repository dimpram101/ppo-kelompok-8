class NewtonMethod { 
  private String func, df, ddf;
  private double x;
  private int n;
  public NewtonMethod(double x, int n){
    this.x = x;
    this.n = n;
  }

  public double f(double x) {
    return (double) (4*Math.log(x)-x);
  }

  public double df(double x) {
    return (double) ((4/x)-1);    
  }

  public double ddf(double x) {
    return (double) (-1*(4/Math.pow(this.x, 2)));
  }

  public void solve() {
    System.out.println("x0 = " + this.x);
    System.out.println("f(x) = " + f(this.x));
    
    for(int i = 0; i < this.n; i++) {
      this.x = this.x - (double)(df(this.x)/ddf(this.x));
      System.out.println("x"+ (i+1) + " = " + this.x);
      System.out.println("f(x) = " + f(this.x));
    }
    System.out.println("Nilai maksimum = " + f(this.x));
  }

  public static void main(String[] args) {
    NewtonMethod soal1 = new NewtonMethod(6, 3);

    soal1.solve();

    System.out.println((float)2/3-1);
  }
}