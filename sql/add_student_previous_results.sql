-- Run this in the Supabase SQL Editor before deploying code that writes
-- previous academic results. Safe to run more than once; existing student
-- records remain valid because all new columns are nullable.
ALTER TABLE public.students
    ADD COLUMN IF NOT EXISTS previous_exam_name varchar(150),
    ADD COLUMN IF NOT EXISTS previous_exam_year integer,
    ADD COLUMN IF NOT EXISTS previous_institution_name varchar(200),
    ADD COLUMN IF NOT EXISTS previous_gpa numeric(5, 2),
    ADD COLUMN IF NOT EXISTS previous_result_details text;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'students_previous_exam_year_range'
          AND conrelid = 'public.students'::regclass
    ) THEN
        ALTER TABLE public.students
            ADD CONSTRAINT students_previous_exam_year_range
            CHECK (previous_exam_year IS NULL OR previous_exam_year BETWEEN 1900 AND 2100);
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'students_previous_gpa_range'
          AND conrelid = 'public.students'::regclass
    ) THEN
        ALTER TABLE public.students
            ADD CONSTRAINT students_previous_gpa_range
            CHECK (previous_gpa IS NULL OR previous_gpa BETWEEN 0 AND 5);
    END IF;
END $$;
