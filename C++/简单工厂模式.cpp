#include<iostream>
#include<string>

using namespace std;

// �����Ʒ��Dog 
class Dog
{
	public:
		void sound(){ cout << "wang wang" << endl; }
		virtual void introduce()=0;
	
};

// �����Ʒ�ࣺС������ 
class RollDog : public Dog
{
	void introduce()
	{
		cout << "my ear is roll ";
		sound(); 
	}
};

// �����Ʒ�ࣺ С������ 
class StraightDog : public Dog
{
	void introduce()
	{
		cout << "my ear is straight ";
		sound();
	}
	
};

// ������ 
class DogStore
{
	public:
	Dog* dog_create(string name)
	{
		if(name == "RollDog")
			return new RollDog();
		else if(name == "StraightDog")
			return new StraightDog();
	}
	
};


int main()
{
	DogStore factory;
	Dog *rd = factory.dog_create("RollDog");
	rd->introduce();
	Dog *sd = factory.dog_create("StraightDog");
	sd->introduce();
	delete rd;
	delete sd;
	 
	return 0;
 } 
