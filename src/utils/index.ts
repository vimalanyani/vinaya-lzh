export const basePath = "/vinaya-lzh";
export const siteName = "Translations of the Chinese Bhikkhunī Vinayas";
export const descriptionPrefix = "Vimalanyani Bhikkhunī’s English translation of ";

export const createAnchor = (text: string) => {
  return text.replace(/ /g, "-").toLowerCase();
};

export const getSchoolPathFilePath = (path: string) => path.split(/(?=\/)/)[0];
