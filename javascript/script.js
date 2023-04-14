  const musicasList = document.getElementById('musicas-list');
  const musicas = Array.from(musicasList.children);

  musicas.sort((a, b) => {
    const musicaA = a.textContent.toUpperCase();
    const musicaB = b.textContent.toUpperCase();
    if (musicaA < musicaB) {
      return -1;
    }
    if (musicaA > musicaB) {
      return 1;
    }
    return 0;
  });

  musicas.forEach((musica) => {
    musicasList.appendChild(musica);
  });