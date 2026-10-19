<%*
// Crée la fiche de révision de la séance courante et pose le lien retour dans
// son frontmatter `review:`. À lancer depuis la note de séance.
const seance = tp.config.active_file;

if (!seance || !seance.path.startsWith("01 courses/lectures/")) {
    new Notice("À lancer depuis une note de séance.");
    return;
}

const nom = seance.basename;
const code = nom.split(" - ")[0];
const court = code.split("-").slice(-2).join("-");
const matiere = seance.parent.name;
const chemin = "01 courses/__reviews/" + nom + ".md";

const existante = app.vault.getAbstractFileByPath(chemin);
if (existante) {
    new Notice("La révision existe déjà.");
    await app.workspace.getLeaf(false).openFile(existante);
    return;
}

// On ne lie que ce qui existe : un wikilink mort ne rend service à personne.
const lignes = [];
for (const [cle, dossier] of [["slides", "slides"], ["exercices", "exercises"]]) {
    const cible = "01 courses/" + dossier + "/" + matiere + "/" + nom + ".md";
    if (app.vault.getAbstractFileByPath(cible)) {
        lignes.push(cle + ': "[[01 courses/' + dossier + "/" + matiere + "/" + nom + ']]"');
    }
}

const contenu = ["---", ...lignes, "---", "- [ ] ", ""].join("\n");
const revision = await tp.file.create_new(contenu, nom, false, "01 courses/__reviews");

await app.fileManager.processFrontMatter(seance, (fm) => {
    const lien = "[[01 courses/__reviews/" + nom + "|Review " + court + "]]";
    const deja = Array.isArray(fm.review) ? fm.review : (fm.review ? [fm.review] : []);
    fm.review = [...deja, lien];
});

await app.workspace.getLeaf(false).openFile(revision);
-%>
