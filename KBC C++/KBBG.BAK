#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<fstream.h>
#include<stdlib.h>

class stud
{
 int rno,correct;
 char ques[50],name1[20],name2[20],name3[20];
 public:
 void m();
 void enter();
 void addnew();
 void recplay(int);
 void wise();
 int roll();
 void delet(int);
 void check();
 int retme(int);
 void showme();
 void shows();
 int right();
};
int stud::roll()
{
 return rno;
}
void stud::showme()
{
  ifstream fin;
  fin.open("bhu.dat",ios::binary|ios::in);
  stud s;
  char line[256];
  int count=0;
  while(fin.read((char *) &s, sizeof(stud)))
  {
  count++;
  s.shows();
  }
  cout<<"\n\n\t\tNo Of Records Are -> "<<count<<endl;
}
void stud::shows(){

  cout<<"\t\t QUESTION  "<<ques<<endl;
  cout<<"\n\t\t1."<<name1<<endl;
  cout<<"\n\t\t2."<<name2<<endl;
  cout<<"\n\t\t3."<<name3<<endl;
  cout<<"\n\n\n\t Choice :-  "<<correct;
}
void stud::addnew()
{ system("cls");
  ofstream fil;
  fil.open("bhu.dat",ios::binary|ios::app);
  stud s;
  char ch;
  do{
    s.enter();
    fil.write((char *) &s, sizeof(stud));
    cout<<"\n\n\tMore(y/n) ?";
    ch = getch();
  }while(ch!='n');
  fil.close();
}
void stud::enter()
{
 cout<<"Enter Question No  ";
 cin>>rno;
 cout<<"\n\n\t"<<" Q-> ";
 gets(ques);
 cout<<"\n\n\t"<<"1.";
 gets(name1);
 cout<<"\n\n\t"<<"2.";
 gets(name2);
 cout<<"\n\n\t"<<"3.";
 gets(name3);
 cout<<"\n\n\t"<<"R=> ";
 cin>>correct;
}
void stud::recplay(int o)
{
  int choice;
  ifstream fin;
  fin.open("bhu.dat",ios::binary);
  stud s;
  while(fin.read((char *) &s, sizeof(stud)))
  { if(s.roll()==o)
    {
     s.shows();
    }
  }
}
int count=0;
void stud::wise(){
  char yes;
  stud s;
  int ret;
  ifstream fin;
  int choice;
  fin.open("bhu.dat",ios::binary);
 while(1){
  int t = random(11-1+1)+1;
    fin.read((char *) &s, sizeof(stud));
    if (s.roll()==t)
    {
  system("cls");
  cout<<"\t\t QUESTION  "<<s.ques<<endl;
  cout<<"\n\t\t1."<<s.name1<<endl;
  cout<<"\n\t\t2."<<s.name2<<endl;
  cout<<"\n\t\t3."<<s.name3<<endl;
  cout<<"\n\t\t\t Enter Your Choice: ";
  cin>>choice;
  fin.open("bhu.dat",ios::binary);
    fin.read((char *) &s, sizeof(stud));
    if (s.correct==choice){
       cout<<"Correct";
       char*p="\n\nPLZZ PRESS ANY KEY TO CONTINUE";
       cout<<p;
       char ch=getch();
       fin.close();
       count=count+1;
       wise();
       }
       else{
       cout<<"Incorrect";
       cout<<"\n\nTotal Coreect Answers =>  "<<count;
       char*p="\n\nPLZZ PRESS ANY KEY TO CONTINUE";
       cout<<p;
       char cl=getch();
       fin.close();
       exit(0);}
       };
    }
}
void stud::delet(int n)
{
	stud s;
	ifstream inFile;
	ofstream outFile;
	inFile.open("bhu.dat",ios::binary|ios::in);
	if(!inFile)
	{
		cout<<"File could not be open !! Press any Key...";
		return;
	}
	outFile.open("Tem.dat",ios::binary|ios::out);
	inFile.seekg(0,ios::beg);
	while(inFile.read((char *) &s, sizeof(stud)))
	{
		if(s.roll()!=n)
		{
		  outFile.write((char *) &s, sizeof(stud));
		}
	}
	inFile.close();
	outFile.close();
	remove("bhu.dat");
	rename("Tem.dat","bhu.dat");
	cout<<"\n\n\tRecord Deleted ..";
}
 int num,ck,n;
 char ch;
 stud y;
void stud::m()
{
 system("cls");


	     do{
		system("cls");
		cout<<"\n\n\n\tMAIN MENU";
		cout<<"\n\n\t01. NEW RECORD";
		cout<<"\n\n\t02. QUERY QUESIONS";
		cout<<"\n\n\t03. SHOW QUESTIONS";
		cout<<"\n\n\t04. RECORD DELETE";
		cout<<"\n\n\t05. SHOW ALL ";
		cout<<"\n\n\t06. EXIT";
		cout<<"\n\n\tSelect Your Option (1-5) ";
		ch=getch();
		system("cls");
		switch(ch)
		{
		case '1':
			y.addnew();
			break;
		case '2':
			cout<<"Which Question Query: " ;
			cin>>n;
			y.recplay(n);
			break;
		case '3':
			y.wise();
			break;
		case '4':
			cout<<"Which Ques: ";
			cin>>n;
			y.delet(n);
			break;
		case '5':
			cout<<"RECORDS ARE =>  ";
			y.showme();
			break;
		case '6':
			cout<<"\n\n\tThanks for using Record managemnt system";
			exit(0);
			break;
		 default :cout<<"\a";
		}
		getch();
    }while(ch!='6');

}
int main()
{
system("cls");
stud y;
y.m();
return(0);
}
