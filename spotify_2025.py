import pandas as pd
import matplotlib.pyplot as plt

dados_2025 = {
    "Musica": [
        "Bellakeo",
        "Macetando",
        "Zona de Perigo",
        "Envolver",
        "Leão",
        "Nosso Quadro",
        "Erro Gostoso"
    ],
    "Artista": [
        "Anitta & Peso Pluma",
        "Ivete Sangalo & Ludmilla",
        "Léo Santana",
        "Anitta",
        "Marília Mendonça",
        "Ana Castela",
        "Simone Mendes"
    ],
    "Streams_milhoes": [
        546,
        800,
        750,
        722,
        495,
        680,
        710
    ]
}


df = pd.DataFrame(dados_2025)

print( " TABELA - Spotify Brasil 2025")
print(df.to_string(index=False))

df = df.sort_values(by="Streams_milhoes", ascending=True)

print(" Ranking por Streams")
print(df[["Musica", "Streams_milhoes"]].to_string(index=False))


spotify_green = "#1DB954"
spotify_black = "#121212"
spotify_white = "#FFFFFF"

plt.figure(figsize=(12, 7))
ax = plt.gca()

ax.set_facecolor(spotify_black)
plt.gcf().patch.set_facecolor(spotify_black)

barras = plt.barh(
    df["Musica"],
    df["Streams_milhoes"],
    color=spotify_green
)

for barra in barras:
    largura = barra.get_width()
    plt.text(
        largura + 10,
        barra.get_y() + barra.get_height()/2,
        f'{largura}M',
        va='center',
        color=spotify_white,
        fontsize=10
    )

plt.xlabel("Streams (milhões)", color=spotify_white)
plt.title(" Top Músicas Brasileiras - Spotify 2025",
          color=spotify_white,
          fontsize=16,
          fontweight='bold')

plt.xticks(color=spotify_white)
plt.yticks(color=spotify_white)

for spine in ax.spines.values():
    spine.set_visible(False)

plt.grid(axis='x', linestyle='--', alpha=0.2)

plt.tight_layout()
plt.show()
