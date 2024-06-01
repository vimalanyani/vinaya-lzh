import type { BookData } from "../data/types";

export const basePath = "/vinaya-lzh";
export const siteName = "Translations of the Chinese Bhikkhunī Vinayas";
export const descriptionPrefix =
  "Vimalañyāṇī Bhikkhunī ’s English translation of ";
export const dateFirstPublished = "2024-05-26";

const bookRenderOrder = ["pm", "vb", "pn", "gd"];

export const orderBookData = (bookData: BookData[]) => {
  return bookData.sort((a, b) => {
    const book1 = a.path.split("/").pop()!;
    const book2 = b.path.split("/").pop()!;
    return bookRenderOrder.indexOf(book1) - bookRenderOrder.indexOf(book2);
  });
};

export const createAnchor = (text: string) => {
  return text.replace(/ /g, "-").toLowerCase();
};

export const getSchoolPathFilePath = (path: string) => path.split(/(?=\/)/)[0];
