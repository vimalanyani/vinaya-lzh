import { promises as fs } from "fs";
import path from "path";
import type { RuleData } from "../data/types";

export const rulePaths = {
  mgbv: "/mg/vb",
} as const;

type RulePath = (typeof rulePaths)[keyof typeof rulePaths];

async function getAllBookRuleData({
  rulePath,
}: {
  rulePath: RulePath;
}): Promise<RuleData[]> {
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
