import { promises as fs } from "fs";
import path from "path";
import type { RuleData, RuleDirPath } from "../data/types";

async function checkPathExists(filePath: string) {
  try {
    const stats = await fs.stat(filePath);
    return Boolean(stats);
  } catch (error) {
    return false;
  }
}

async function getAllBookRuleData({
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

export default getAllBookRuleData;
