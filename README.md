# AeroDesign Auto
![GitHub License](https://img.shields.io/github/license/Polluix/aerodesign-auto)

# Sobre o projeto

Automatização da aquisição de dados do software Aerodesign Propeller Selector.

A aplicação consiste na automatização do mouse para alteração dos inputs do software e do processamento de screenshots de sua interface principal com os resultados, posteriormente escritos em um arquivo .txt no mesmo diretório de instalação do programa. O robô diminui o tempo necessário para gerar arquivos de dados para diversas
configurações de conjunto motopropulsor drasticamente.

# Tecnologias Utilizadas
- Python 3.11.0

## Controle de dependências
- Poetry
  
## Automatização do mouse
- PyAutoGUI

## Processamento dos dados
- Numpy

## Processamento de imagem
- Pillow
- EasyOCR
- OpenCV-Python

## Build do programa
- PyInstaller

# Requisitos
Aerodesign Propeller Selector: https://www.hoppenbrouwer-home.nl/ikarus/software/propselector.htm

# Como utilizar o programa
1. Faça Download do instalador
2. Siga os passos descritos na interface de instalação.
3. Abra o Extended Propeller Selector.
4. Insira as configurações desejadas para propeller diameter, propeller pitch, number of blades e RPM.

**NOTA IMPORTANTE**: não altere nenhuma outra propriedade no Extended Propeller Selector ou o programa poderá
   não funcionar corretamente.
   
6. Execute o AeroDesign Auto como administrador, sem minimizar o Extended Prop Selector.
7. Aguarde a execução dos comandos pelo robô.

# Output do Programa
- data.txt: contém os dados obtidos do processamento de imagens do Extended Propeller Selector.
- image.png: última screenshot tirada pelo robô.

Ambos arquivos são gerados no diretório de instalação do programa.

**NOTA IMPORTANTE**: O processamento das screenshots pode apresentar problemas. O próprio programa contorna
problemas conhecidos, porém, dados incorretos podem ser escritos no arquivo. É dever do usuário verificar o
resultado final e realizar ajustes finos quando necessário.

# Após a execução

O arquivo data.txt deve ser movido para outro diretório e image.png pode ser mantido ou excluído

# Autor
Luiz Felipe Camargo Souza

https://www.linkedin.com/in/lufelcamargo

