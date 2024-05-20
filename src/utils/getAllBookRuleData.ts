import { promises as fs } from "fs";
import path from "path";
import type { RuleData } from "../data/types";

export const rulePrimaryGroups = {
  mgBv: { name: "Bhikkhunī Vibhaṅga", path: "/mg/vb" },
  mgGd: { name: "Garudhammas", path: "/mg/gd" },
  mgPn: { name: "Bhikkhunī Pakiṇṇaka", path: "/mg/pn" },
} as const;

const rulePaths = Object.values(rulePrimaryGroups).map((group) => group.path);
type RulePath = (typeof rulePaths)[number];;

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
