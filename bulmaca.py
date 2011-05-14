#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       
#       Copyright 2011 Uğurcan <ugurcan@pavilion>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#   Girintilemeler 4 boşluklu sekme(tab) olarak yapılmıştır    
from Tkinter import *
class bulmaca:
	def __init__(self):
		self.bul=["abchardcoralse","dbfzyjmtagdceg","hlilifatollsjr","hecosystemsksk","matjtiaxpsakms"
		,"gcidskrdfpzymu","mhgyhomejovjql","miaeflehpudnnl","hnwpfrttlyffgo"
		,"ighplyhulrlgum","kiuanemoneuodt","klrerbbnrcjhph","ioilyocmjxtjud","clasoftcoralso"]
		self.ara=["coralreefs","bleaching","home","atolls","ecosystems","anemone","polyp","hardcorals","softcorals","mollusk"]
		self.aran=[i for i in self.ara]
		self.nerede={} #nerede sozlugu kelimelerin yerlerini kaydedecek anahtarlar kelimeler degerler yer parametrelerini icerecek
	def kelimeAra(self,kbul,yon):
		#kelimeyi buldum ama direk kaydedemem yatay mı dusey mı capraz mı bilmem lazım diye bir yon degiskeni tuttum 
		#1->yatay
		#2->dusey
		#3->sol capraz
		#4->sag capraz
		#tersler içinde yon*11 
		for satir in kbul:
			for kelime in self.ara:
				yer=satir.find(kelime)
				if (yer != -1):
					if (yon%11==0):
						yer=self.bul.__len__()-yer-1
					#Farklı string dizileri kullandığım için koordinat dönüşümlerini yapan if blokları
					if(yon==1 or yon==11):
						self.nerede[kelime]=[yon,kbul.index(satir),yer,kelime.__len__()]
						#nerede degerlerinin meali su sekilde hangi yonde kacinci satir veya sutunda 
						#kacinci karekterden basliyor uzunlugu ne kadar
					if(yon==2 or yon==22):
						self.nerede[kelime]=[yon,yer,kbul.index(satir),kelime.__len__()]
					if(yon==3 or yon==33):
						if(yer<13):
							self.nerede[kelime]=[yon,self.bul.__len__()-1-satir.__len__()-1+yer,yer,kelime.__len__()]
						else:
							self.nerede[kelime]=[yon,self.bul.__len__()-1- satir.__len__()-1+(yer%14),yer%14,kelime.__len__()]
					if(yon==4 or yon==44):
						if (yer<13):
							self.nerede[kelime]=[yon,satir.__len__()-1-yer,yer,kelime.__len__()]
						else:
							self.nerede[kelime]=[yon,self.bul.__len__()-satir.__len__()+yer%14,self.bul.__len__()-yer%14-1,kelime.__len__()]
					self.ara.remove(kelime)
					#arama sonucu sözlüğe eklendikten sonra kelime arama listesinden silinir.
	def yatayAra(self):
		self.kelimeAra(self.bul,1)
		self.kelimeAra([i[::-1] for i in self.bul],11)
		#Bir liste üreteci ile yatay liste ters çevrilir.
	def duseyAra(self):
		self.dusey=[]
		for i in range(0,14):
			temp=""
			for satir in self.bul:
				temp+=satir[i]
			self.dusey.append(temp)
		self.kelimeAra(self.dusey,2)
		self.kelimeAra([i[::-1] for i in self.dusey],22)
	def solCaprazAra(self):
		self.solcapraz=[]
		self.temp=[]
		#Köşegenin altının ve üstünün oluşturulması için farklı for döngüleri kullanılır.
		for i in range(1,self.bul.__len__()+1):
			temp=""
			for j in range(1,i+1):
				temp+=self.bul[i-j][self.bul.__len__()-j]
			self.solcapraz.append(temp[::-1])
		for i in range(1,self.bul.__len__()):
			temp=""
			for j in range(1,i+1):
				temp+=self.bul[self.bul.__len__()-i+j-1][j-1]
			self.temp.append(temp)
		self.temp.reverse()
		#Listeyi ters çevirir
		self.solcapraz.extend(self.temp)
		self.kelimeAra(self.solcapraz,3)
		self.kelimeAra([i[::-1] for i in self.solcapraz],33)
	def sagCaprazAra(self):
		self.sagcapraz=[]
		ltemp=[]
		for i in range(1,self.bul.__len__()+1):
			temp=""
			for j in range(1,i+1):
				temp+=self.bul[j-1][i-j]
			self.sagcapraz.append(temp)
		for i in range(1,self.bul.__len__()+1):
			temp=""
			for j in range(1,i+1):
				temp+=self.bul[self.bul.__len__()-i+j-1][self.bul.__len__()-j]
			ltemp.append(temp)
		ltemp.reverse()
		self.sagcapraz.extend(ltemp)
		self.kelimeAra(self.sagcapraz,4)
		self.kelimeAra([i[::-1] for i in self.sagcapraz],44)
	def arama(self):
		#Arama ve işaretlemeyi kolaylık olsun diye bir metodda topladım.
		self.yatayAra()
		self.duseyAra()
		self.solCaprazAra()
		self.sagCaprazAra()
		self.isaret(self.nerede)
	def isaret(self,sozluk):
		self.fobul=[[j for j in i] for i in self.bul]
		#Metin listesinden karakter matrisi elde eden liste üreteci
		for kelime in sozluk:
			for i in range(0,sozluk[kelime][3]):
				#Bulunan kelimelerin harfleri büyütülür
				if (sozluk[kelime][0]== 1):
					self.fobul[sozluk[kelime][1]][sozluk[kelime][2]+i]=self.bul[sozluk[kelime][1]][sozluk[kelime][2]+i].upper()
				if (sozluk[kelime][0]==11):
					self.fobul[sozluk[kelime][1]][sozluk[kelime][2]-i]=self.bul[sozluk[kelime][1]][sozluk[kelime][2]-i].upper()
				if (sozluk[kelime][0]==2):
					self.fobul[sozluk[kelime][1]+i][sozluk[kelime][2]]=self.bul[sozluk[kelime][1]+i][sozluk[kelime][2]].upper()
				if (sozluk[kelime][0]==22):
					self.fobul[sozluk[kelime][1]-i][sozluk[kelime][2]]=self.bul[sozluk[kelime][1]-i][sozluk[kelime][2]].upper()
				if (sozluk[kelime][0]==3):
					self.fobul[sozluk[kelime][1]+i][sozluk[kelime][2]+i]=self.bul[sozluk[kelime][1]+i][sozluk[kelime][2]+i].upper()
				if(sozluk[kelime][0]==33):
					self.fobul[sozluk[kelime][1]-i][sozluk[kelime][2]-i]=self.bul[sozluk[kelime][1]-i][sozluk[kelime][2]-i].upper()
				if (sozluk[kelime][0]==4):
					self.fobul[sozluk[kelime][1]+i][sozluk[kelime][2]-i]=self.bul[sozluk[kelime][1]+i][sozluk[kelime][2]-i].upper()
				if(sozluk[kelime][0]==44):
					self.fobul[sozluk[kelime][1]-i][sozluk[kelime][2]+i]=self.bul[sozluk[kelime][1]-i][sozluk[kelime][2]+i].upper()
		self.fobul=["".join(i) for i in self.fobul]
		#karakter matrisi metin listesi olarak tekrar birleştirilir
		self.metin_ui()
	def metin_ui(self,renk="red"):
		for i in range(0,self.fobul.__len__()):
			for j in range(0,self.fobul.__len__()):
				#Daha önce isaret metodunda büyütülmüş harfler renkli diğerleri siyah olarak ekrana yazdırılır.
				if (self.fobul[j][i].isupper()):
					etiket=Label(text=self.fobul[j][i],bg="white",fg=renk,font="Verdana 20")
					etiket.place(relx=0.0+(i*0.05),rely=0.0+(j*0.07),relheight=0.07,relwidth=0.05)	
				else:
					etiket=Label(text=self.fobul[j][i].upper(),bg="white",font="Verdana 20")
					etiket.place(relx=0.0+(i*0.05),rely=0.0+(j*0.07),relheight=0.07,relwidth=0.05)
	def tik(self):
		self.chosenOne=[]
		bul=Label(text="Aranacak Kelimeler",font="Verdana 12 bold")
		bul.place(relx=0.70,rely=0.040,relheight=0.05,relwidth=0.3)
		for i in range(0,self.aran.__len__()):
			temp=IntVar()
			temp.set(0)
			#Kutucuk durumunu tutacak Tkinter değişkeni tanımlanır
			self.chosenOne.append(temp)
			onay=Checkbutton(text="",variable=self.chosenOne[i])
			onay.place(relx=0.75,rely=0.090+(i*0.05),relheight=0.05,relwidth=0.05)
			etiket=Label(text=self.aran[i].capitalize())
			etiket.place(relx=0.80,rely=0.0913+(i*0.05),relheight=0.05,relwidth=0.15)
			#Kutucuklar yerleştirilir.
		etiket=Label(text="Tekrar Arama")
		etiket.place(relx=0.75,rely=0.55,relheight=0.075,relwidth=0.2)
		tamam=Button(text="Secimle",command=self.tikSecim)
		tamam.place(relx=0.73,rely=0.65,relheight=0.075,relwidth=0.1)
		varsay=Button(text="Varsayılan",command=lambda: self.isaret(self.nerede))
		varsay.place(relx=0.88,rely=0.65,relheight=0.075,relwidth=0.1)
		#Tekrar Arama işlemini yapacak butonlar tanımlanır.
	def tikSecim(self):
		self.secim={}
		for i in range(0,self.aran.__len__()):
			if(self.chosenOne[i].get()==1):
				self.secim[self.aran[i]]=self.nerede[self.aran[i]]
			#Kutucuklardan yapılan seçimler doğrultusunda yeni bir arama sözlüğü oluşturulur ve işaret fonksyonuna gönderilir.
		self.isaret(self.secim)
	def anaMenu(self):
		ana=Menu(pencere)
		pencere.config(menu=ana)
		secim=Menu(ana, tearoff=0)
		ana.add_cascade(label="Renk",menu=secim)
		#menü başlığı tanımlanır.
		secim.add_command(label="Kirmizi",command=lambda: self.metin_ui("red"))#normalde command deyimi üzerinden çağrılan fonksyon
		secim.add_command(label="Mavi",command=lambda: self.metin_ui("blue"))  #lara parametre gönderemiyoruz ancak tam fonksyon çağrı
		secim.add_command(label="Yesil",command=lambda: self.metin_ui("green"))#mızı bir lambda fonksyonunda yapıp command deyimine
		secim.add_command(label="Sari",command=lambda: self.metin_ui("yellow"))#lambda fonksyonunu gönderdiğimizde bu hatayı aşabiliyoruz
		secim.add_command(label="Mor",command=lambda: self.metin_ui("purple"))
		#menü elemanları tanımlanır
ornek = bulmaca()
pencere=Tk()
ornek.arama()
ornek.anaMenu()
ornek.tik()
pencere.geometry("700x450")
pencere.title("Kelime Bulmaca")
mainloop()
