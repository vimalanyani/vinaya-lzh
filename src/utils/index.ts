import type { RuleData, RuleDirPath, BookData } from "../data/types";
import { promises as fs } from "fs";
import path from "path";

/*
 * CONSTANTS
 *
 */

export const basePath = "/vinaya-lzh";

/*
 * BOOK HANDLING
 *
 */

const bookRenderOrder = ["pm", "vb", "pn", "gd", "kd"];
export const orderBookData = (bookData: BookData[]) => {
  return bookData.sort((a, b) => {
    const book1 = a.path.split("/").pop()!;
    const book2 = b.path.split("/").pop()!;
    return bookRenderOrder.indexOf(book1) - bookRenderOrder.indexOf(book2);
  });
};

async function checkPathExists(filePath: string) {
  try {
    const stats = await fs.stat(filePath);
    return Boolean(stats);
  } catch (error) {
    return false;
  }
}

export async function getAllBookRuleData({
  rulePath,
}: {
  rulePath: RuleDirPath;
}): Promise<RuleData[]> {
  const fullPath = path.join(process.cwd(), `src/data${rulePath}/json`);

  if (!(await checkPathExists(fullPath))) {
    return [];
  }

  const directory = path.join(process.cwd(), `src/data${rulePath}/json`);

  const filenames = await fs.readdir(directory);

  const files = filenames.map(async (filename) => {
    const filePath = path.join(directory, filename);

    const fileContents = await fs.readFile(filePath, "utf8");
    return JSON.parse(fileContents) as RuleData;
  });
  return Promise.all(files);
}

/*
 * GENERAL
 *
 */

export const createAnchor = (text: string) => {
  return text.replace(/ /g, "-").toLowerCase();
};

export const getSchoolPathFilePath = (path: string) => path.split(/(?=\/)/)[0];
