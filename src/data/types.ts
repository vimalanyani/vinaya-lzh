import { ruleDirPaths, schoolBookGroups } from "../data/content";

interface RuleBody {
  h2: string;
  lzh: string[];
  en: string[];
  en_verse: string[];
  lzh_grouping_info: string[];
  en_grouping_info: string[];
}

export interface RuleData {
  id: string;
  school: string;
  book: string;
  rule_class: string;
  rule_no: string;
  body: RuleBody[];
  file: string;
  prev_file: string | null;
  next_file: string | null;
}

export type RuleDirPath = (typeof ruleDirPaths)[number];

export type BookData = {
  data: RuleData[];
  path: string;
  schoolName: string;
  bookName: string;
};
