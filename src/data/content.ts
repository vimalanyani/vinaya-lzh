// Render order: patimokkha, vibhanga, pakinnaka, garudhammas.

export const schoolBookGroups = {
  mg: [
    {
      path: "/mg/pm",
      schoolName: "Mahāsaṅghika",
      bookName: "Bhikkhunī Pātimokkha",
    },
    {
      path: "/mg/vb",
      schoolName: "Mahāsaṅghika",
      bookName: "Bhikkhunī Vibhaṅga",
    },
    {
      path: "/mg/pn",
      schoolName: "Mahāsaṅghika",
      bookName: "Bhikkhunī Pakiṇṇaka",
    },
    {
      path: "/mg/gd",
      schoolName: "Mahāsaṅghika",
      bookName: "Bhikkhunī Garudhamma",
    },
  ],
  mi: [
    {
      path: "/mi/pm",
      schoolName: "Mahīśāsaka",
      bookName: "Bhikkhunī Pātimokkha",
    },
    {
      path: "/mi/vb",
      schoolName: "Mahīśāsaka",
      bookName: "Bhikkhunī Vibhaṅga",
    },
    {
      path: "/mi/dm",
      schoolName: "Mahīśāsaka",
      bookName: "Bhikkhunī Dhammaka",
    }
  ],
  dg: [
    {
      path: "/dg/pm",
      schoolName: "Dharmaguptaka",
      bookName: "Bhikkhunī Pātimokkha",
    },
    {
      path: "/dg/vb",
      schoolName: "Dharmaguptaka",
      bookName: "Bhikkhunī Vibhaṅga",
    },
    {
      path: "/dg/pn",
      schoolName: "Dharmaguptaka",
      bookName: "Bhikkhunī Pakiṇṇaka",
    },
    {
      path: "/dg/gd",
      schoolName: "Dharmaguptaka",
      bookName: "Bhikkhunī Garudhamma",
    },
    {
      path: "/dg/kd",
      schoolName: "Dharmaguptaka",
      bookName: "Bhikkhunī Khandhaka",
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
      path: "/sarv/dm",
      schoolName: "Sarvāstivāda",
      bookName: "Bhikkhunī Dhammaka",
    },
    {
      path: "/sarv/pm",
      schoolName: "Sarvāstivāda",
      bookName: "Bhikkhunī Pātimokkha",
    },
  ],
  mu: [
    {
      path: "/mu/pm",
      schoolName: "Mūlasarvāstivāda",
      bookName: "Bhikkhunī Pātimokkha",
    },
    {
      path: "/mu/vb",
      schoolName: "Mūlasarvāstivāda",
      bookName: "Bhikkhunī Vibhaṅga",
    },
    {
      path: "/mu/pn",
      schoolName: "Mūlasarvāstivāda",
      bookName: "Bhikkhunī Pakiṇṇaka",
    },
    {
      path: "/mu/gd",
      schoolName: "Mūlasarvāstivāda",
      bookName: "Bhikkhunī Garudhamma",
    },
  ],
} as const;

export const ruleDirPaths = Object.values(schoolBookGroups)
  .map((school) => school.map((book) => book.path))
  .flat();
