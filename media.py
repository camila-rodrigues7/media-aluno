# coding: utf-8
from MediaNotas import MediaNotas
import pdb
import random

nome_aluno = str(input("Informe o nome do aluno: "))
notas = []

pdb.set_trace()

for i in range(0,3):
	nota = float(input('Informe a nota do aluno: '))
	notas.append(nota)

	media_notas = MediaNotas(nome_aluno, notas)
	media = media_notas.calcular_media()
	print(media)
