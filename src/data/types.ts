interface RuleSection {
  heading: string;
  parts: {
    lzh: string[];
    en: string[];
  }[];
}

export interface RuleData {
  id: string;
  school: string;
  book: string;
  rule_class: string;
  rule_no: string;
  sections: RuleSection[];
  file: string;
  prev_file: string | null;
  next_file: string | null;
}
