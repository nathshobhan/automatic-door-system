import processing.serial.*;

Serial x;
void setup()
{
size(640,480);
x=new Serial(this,"COM3",9600);
}
void draw()
{
if(x.available()>0)
{
int z=x.read();
println(z);
if(z>20)
{
String abc="1";
String[] b=split(abc," ");
saveStrings("file.txt",b);


}


}


}