#include<iostream>
#include<string>

using namespace std;

// 抽象产品类
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

//抽象工厂类 
class Store
{
	virtual Dog* dog_create()=0;
 }; 

//具体工厂类 
class RollStore: public Store
{
	
	public:
	Dog* dog_create()
	{
		return new RollDog();
	}
	
};

//具体工厂类 
class StraightStore: public Store
{
	public:
	Dog* dog_create()
	{
		return new StraightDog();
	}
	
};




int main()
{
	RollStore factory1;
	Dog *rd = factory1.dog_create();
	rd->introduce();
	
	StraightStore factory2;
	Dog *sd = factory2.dog_create();
	sd->introduce();
	
	delete rd;
	delete sd;
		
	return 0;
 } 
