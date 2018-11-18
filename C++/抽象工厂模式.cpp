#include<iostream>
#include<string>

using namespace std;

// 抽象产品类1
class Dog
{
	public:
		void sound(){ cout << "wang wang" << endl; }
		virtual void introduce()=0;
	
};

// 具体产品类：卷耳狗
class RollDog : public Dog
{
	void introduce()
	{
		cout << "my ear is roll ";
		sound(); 
	}
};

// 具体产品类： 直耳狗
class StraightDog : public Dog
{
	void introduce()
	{
		cout << "my ear is straight ";
		sound();
	}
	
};

// 抽象产品类2
class Cat
{
	public:
		void sound(){ cout << "miao miao" << endl; }
		virtual void introduce()=0;
	
};

// 具体产品类
class StraightCat : public Cat
{
	void introduce()
	{
		cout << "my ear is straight ";
		sound(); 
	}
};

// 具体产品类
class RollCat : public Cat
{
	void introduce()
	{
		cout << "my ear is roll " ;
		sound();
	}
	
};

//抽象工厂类 
class Store
{
	virtual Dog *dog_create()=0;
	virtual Cat *cat_create()=0;
 }; 

//具体工厂类 
class StraightStore: public Store
{
	
	public:
	Dog* dog_create()
	{
		return new StraightDog();	
	}
	
	Cat* cat_create()
	{
		return new StraightCat();
	}
	
};

//具体工厂类 
class RollStore: public Store
{
	public:
	Dog* dog_create()
	{
		return new RollDog();
	}
	
	Cat* cat_create()
	{
		return new RollCat();
	}
	
};




int main()
{
	StraightStore factory1;
	Dog *sd = factory1.dog_create();
	sd->introduce();
	Cat *sc = factory1.cat_create();
	sc->introduce();
	
	RollStore factory2;
	Dog *rd = factory2.dog_create();
	rd->introduce();
	Cat *rc = factory2.cat_create();
	rc->introduce();	
	
	delete sd;
	delete sc;
	delete rd;
	delete rc;
		
	return 0;
 } 
