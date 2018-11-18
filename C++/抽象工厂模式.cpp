#include<iostream>
#include<string>

using namespace std;

// �����Ʒ��1
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

// �����Ʒ��2
class Cat
{
	public:
		void sound(){ cout << "miao miao" << endl; }
		virtual void introduce()=0;
	
};

// �����Ʒ��
class StraightCat : public Cat
{
	void introduce()
	{
		cout << "my ear is straight ";
		sound(); 
	}
};

// �����Ʒ��
class RollCat : public Cat
{
	void introduce()
	{
		cout << "my ear is roll " ;
		sound();
	}
	
};

//���󹤳��� 
class Store
{
	virtual Dog *dog_create()=0;
	virtual Cat *cat_create()=0;
 }; 

//���幤���� 
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

//���幤���� 
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
