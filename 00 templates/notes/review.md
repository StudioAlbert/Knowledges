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

let revision = app.vault.getAbstractFileByPath("01 courses/__reviews/" + nom + ".md");

if (!revision) {
    // On ne lie que ce qui existe : un wikilink mort ne rend service à personne.
    const lignes = [];
    for (const [cle, dossier] of [["slides", "slides"], ["exercices", "exercises"]]) {
        const cible = "01 courses/" + dossier + "/" + matiere + "/" + nom + ".md";
        if (app.vault.getAbstractFileByPath(cible)) {
            lignes.push(cle + ': "[[01 courses/' + dossier + "/" + matiere + "/" + nom + ']]"');
        }
    }
    const contenu = ["---", ...lignes, "---", "- [ ] ", ""].join("\n");
    revision = await tp.file.create_new(contenu, nom, false, "01 courses/__reviews");
}

// Templater réécrit le buffer de la séance juste après ce template : écrire son
// frontmatter ici se ferait écraser. On repousse après l'insertion.
const lien = "[[01 courses/__reviews/" + nom + "|Review " + court + "]]";
setTimeout(async () => {
    await app.fileManager.processFrontMatter(seance, (fm) => {
        const deja = Array.isArray(fm.review) ? fm.review : (fm.review ? [fm.review] : []);
        if (!deja.includes(lien)) fm.review = [...deja, lien];
    });
    await app.workspace.getLeaf(false).openFile(revision);
}, 0);
-%>
