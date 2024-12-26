# Compatibilidade de música em um grupo de pessoas através do lastFM
## Não sou bom com nomes

O lastFM é um site que permite o usuário salvar suas reproduções musicais, além disso, ele poder seguir amigos e descobrir novas músicas baseado no seu gosto musical.
Quando você visita um perfil, você pode ver qual a sua porcentagem de compatibilidade com outros membros, mas essa é uma relação de 1 para 1 e não são disponibilizadas muitas informações
[Alguns sites permitem o usuário fazer o download desses dados em arquivo CSV](https://lastfm.ghan.nl/export/), então tive a ideia de tentar achar as músicas, álbuns e artistas favoritos/mais compatíveis dado um grupo de pessoas

Utilizei duas técnicas para tentar avaliar, a primeira é mais intuitiva:
- Para descobrir o peso de uma música, divide a quantidade de scrobbles que uma pessoa tem naquela música e divide pela quantidade total de scrobbles que a pessoa tem, e soma com todos os todos os membros, dado por n, para deixar um pouco mais voltado para valorizar músicas ouvidas por mais pessoas, multiplica-se por n

![equation](https://latex.codecogs.com/svg.image?\huge&space;n\cdot\sum_{x=1}^{n}\frac{SM(x)}{ST(x)})

- A outra técnica utiliza uma ideia de logaritmos, para valorizar mais as músicas ouvidas por mais pessoas ao invés de músicas que uma só pessoa escuta muito, a ideia seria tirar o log do número de scrobbles de uma música e somar, mas como a soma dos logs pode ser o log do produto, para essa situação, foi utilizado apenas produto

![equation](https://latex.codecogs.com/svg.image?\huge&space;\bg{white}\sum_{x=1}^{n}\log(SM(x))\equiv\prod_{x=1}^{n}SM(x))

ah sim, eu sei que o código tá porco.

## Como usar
Apenas coloque os arquivos .csv seu e de seus amigos na pasta /users e rode main.py
em /output vão haver os resultados para artista, album e música utilizando os dois métodos apresentados, lá há três campos, o do peso calculado, a música/album/artista e os usuários que escutam o artista
As músicas/albuns/artistas mais compatíveis serão os mais acima no arquivo, com o valor de peso MENOR (os valores são todos negativos)

No repositório estão os resultados que eu obtive.
