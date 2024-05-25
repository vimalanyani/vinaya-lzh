export const basePath = "/vinaya-lzh";
export const siteName = "Translations of the Chinese Bhikkhunī Vinayas";
export const descriptionPrefix =
  "Vimalanyani Bhikkhunī’s English translations of ";

export const createAnchor = (text: string) => {
  return (
    text
      .replace(/ /g, "-")
      // .replace(/[^a-zA-Z0-9-]/g, "")
      .toLowerCase()
  );
};
