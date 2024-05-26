export const schoolBookGroups = {
  mg: [
    {
      path: "/mg/vb",
      schoolName: "Mahāsaṅghika",
      bookName: "Bhikkhunī Vibhaṅga",
    },
    {
      path: "/mg/gd",
      schoolName: "Mahāsaṅghika",
      bookName: "Bhikkhunī Garudhamma",
    },
    {
      path: "/mg/pn",
      schoolName: "Mahāsaṅghika",
      bookName: "Bhikkhunī Pakiṇṇaka",
    },
    {
      path: "/mg/pm",
      schoolName: "Mahāsaṅghika",
      bookName: "Bhikkhunī Pātimokkha",
    },
  ],
  mi: [
    {
      path: "/mi/vb",
      schoolName: "Mahīśāsaka",
      bookName: "Bhikkhunī Vibhaṅga",
    },
    {
      path: "/mi/gd",
      schoolName: "Mahīśāsaka",
      bookName: "Bhikkhunī Garudhamma",
    },
    {
      path: "/mi/pn",
      schoolName: "Mahīśāsaka",
      bookName: "Bhikkhunī Pakiṇṇaka",
    },
    {
      path: "/mi/pm",
      schoolName: "Mahīśāsaka",
      bookName: "Bhikkhunī Pātimokkha",
    },
  ],
  dg: [
    {
      path: "/dg/vb",
      schoolName: "Dharmaguptaka",
      bookName: "Bhikkhunī Vibhaṅga",
    },
    {
      path: "/dg/gd",
      schoolName: "Dharmaguptaka",
      bookName: "Bhikkhunī Garudhamma",
    },
    {
      path: "/dg/pn",
      schoolName: "Dharmaguptaka",
      bookName: "Bhikkhunī Pakiṇṇaka",
    },
    {
      path: "/dg/pm",
      schoolName: "Dharmaguptaka",
      bookName: "Bhikkhunī Pātimokkha",
    },
  ],
  sarv: [
    {
      path: "/sarv/vb",
      schoolName: "Sarvāstivāda",
      bookName: "Bhikkhunī Vibhaṅga",
    },
    {
      path: "/sarv/gd",
      schoolName: "Sarvāstivāda",
      bookName: "Bhikkhunī Garudhamma",
    },
    {
      path: "/sarv/pn",
      schoolName: "Sarvāstivāda",
      bookName: "Bhikkhunī Pakiṇṇaka",
    },
    {
      path: "/sarv/pm",
      schoolName: "Sarvāstivāda",
      bookName: "Bhikkhunī Pātimokkha",
    },
  ],
  mu: [
    {
      path: "/mu/vb",
      schoolName: "Mūlasarvāstivāda",
      bookName: "Bhikkhunī Vibhaṅga",
    },
    {
      path: "/mu/gd",
      schoolName: "Mūlasarvāstivāda",
      bookName: "Bhikkhunī Garudhamma",
    },
    {
      path: "/mu/pn",
      schoolName: "Mūlasarvāstivāda",
      bookName: "Bhikkhunī Pakiṇṇaka",
    },
    {
      path: "/mu/pm",
      schoolName: "Mūlasarvāstivāda",
      bookName: "Bhikkhunī Pātimokkha",
    },
  ],
} as const;

export const ruleDirPaths = Object.values(schoolBookGroups)
  .map((school) => school.map((book) => book.path))
  .flat();
