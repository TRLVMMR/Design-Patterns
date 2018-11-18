#include<iostream>
#include<string>

using namespace std;

// 抽象产品类Dog 
class Dog
{
	public:
		void sound(){ cout << "wang wang" << endl; }
		virtual void introduce()=0;
	
};

// 具体产品类：小狗旺财 
class RollDog : public Dog
{
	void introduce()
	{
		cout << "my ear is roll ";
		sound(); 
	}
};

// 具体产品类： 小狗阿黄 
class StraightDog : public Dog
{
	void introduce()
	{
		cout << "my ear is straight ";
		sound();
	}
	
};

// 工厂类 
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
