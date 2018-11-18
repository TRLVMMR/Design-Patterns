#include<iostream>
#include<string>

using namespace std;

// �����Ʒ��
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

//���󹤳��� 
class Store
{
	virtual Dog* dog_create()=0;
 }; 

//���幤���� 
class RollStore: public Store
{
	
	public:
	Dog* dog_create()
	{
		return new RollDog();
	}
	
};

//���幤���� 
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
